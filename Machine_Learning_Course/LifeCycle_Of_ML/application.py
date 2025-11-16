# ---- paste into app.py (above your routes) ----
import json
from flask import abort

def get_expected_feature_names():
    """
    Return a list of expected feature names (in order).
    If the scaler has feature_names_in_ (sklearn >= 1.0), use that.
    Otherwise fall back to a hardcoded list you define (update if needed).
    """
    # prefer scaler feature names if available
    if hasattr(standard_scaler, "feature_names_in_"):
        return list(standard_scaler.feature_names_in_)
    # fallback - update this to the real order you trained with
    return ["Temperature","RH","Ws","rain","FFMC","DMC","DC","ISI","Classes","Region"]

@application.route("/debug_features", methods=["GET"])
def debug_features():
    """Return what the scaler/model expect (for debugging)."""
    info = {
        "scaler_n_features_in": getattr(standard_scaler, "n_features_in_", None),
        "scaler_feature_names_in": list(getattr(standard_scaler, "feature_names_in_", [])),
    }
    # include model coef shape if available
    try:
        info["ridge_coef_shape"] = getattr(ridge_model, "coef_", None).shape if hasattr(ridge_model, "coef_") else None
    except Exception:
        info["ridge_coef_shape"] = "unavailable"
    return jsonify(info)

# replace your parse_and_validate / prediction logic with this block inside predict_fwi POST handling:
    # determine expected features (ordered)
    expected = get_expected_feature_names()
    # get payload (form or JSON)
    payload = request.get_json() if request.is_json else request.form.to_dict()

    # check missing keys
    missing = [f for f in expected if f not in payload]
    if missing:
        err = f"Missing fields required by model: {missing}. Expected fields (in order): {expected}"
        app.logger.error(err)
        if request.is_json:
            return jsonify({"error": err}), 400
        return render_template("home.html", result=None, error=err), 400

    # build value list in the exact order expected by scaler
    try:
        values = [float(payload[f]) for f in expected]
    except Exception as e:
        err = f"Invalid numeric input for one of expected fields: {str(e)}"
        app.logger.error(err)
        if request.is_json:
            return jsonify({"error": err}), 400
        return render_template("home.html", result=None, error=err), 400

    arr = np.array([values])  # shape (1, n_expected)
    # double-check shape matches scaler expectation
    n_expected = getattr(standard_scaler, "n_features_in_", arr.shape[1])
    if arr.shape[1] != n_expected:
        err = f"Prepared input has {arr.shape[1]} features but scaler expects {n_expected}."
        app.logger.error(err)
        return render_template("home.html", result=None, error=err), 500

    # transform and predict
    try:
        arr_scaled = standard_scaler.transform(arr)
        prediction = ridge_model.predict(arr_scaled)
        pred_value = float(np.squeeze(prediction))
    except Exception as e:
        app.logger.exception("Prediction failed: %s", e)
        if request.is_json:
            return jsonify({"error": "Prediction failed", "details": str(e)}), 500
        return render_template("home.html", result=None, error="Prediction failed: " + str(e)), 500

    # return
    if request.is_json:
        return jsonify({"prediction": pred_value}), 200
    return render_template("home.html", result=round(pred_value,6))
