"""
Machine Learning Mini Model – Linear Regression
================================================
This program demonstrates a complete ML pipeline using scikit-learn:
  1. Data loading / generation
  2. Preprocessing (train/test split, feature scaling)
  3. Model training (Linear Regression)
  4. Prediction
  5. Evaluation (MAE, MSE, R²)

Dataset: California Housing (built into scikit-learn)
Target : Median house value (in $100 000s)
"""

# ── Imports ──────────────────────────────────────────────────────────────────
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ── 1. Data Loading ───────────────────────────────────────────────────────────

def load_data():
    """
    Load the California Housing dataset from scikit-learn.

    Returns
    -------
    X : ndarray, shape (n_samples, n_features)
        Feature matrix (8 numerical housing attributes).
    y : ndarray, shape (n_samples,)
        Target vector – median house value in $100 000s.
    feature_names : list[str]
        Names of the 8 input features.
    """
    dataset = fetch_california_housing()
    X = dataset.data
    y = dataset.target
    feature_names = list(dataset.feature_names)

    print("=" * 55)
    print("  DATASET OVERVIEW")
    print("=" * 55)
    print(f"  Samples  : {X.shape[0]:,}")
    print(f"  Features : {X.shape[1]}")
    print(f"  Features : {feature_names}")
    print(f"  Target   : Median house value ($100k)")
    print()

    return X, y, feature_names


# ── 2. Preprocessing ──────────────────────────────────────────────────────────

def preprocess_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and test sets, then standardise features.

    Standardisation (z-score) ensures that features with large numeric
    ranges (e.g. population) do not dominate features with small ranges
    (e.g. average rooms), which improves gradient-based optimisation.

    Parameters
    ----------
    X            : feature matrix
    y            : target vector
    test_size    : fraction reserved for testing (default 20 %)
    random_state : seed for reproducibility

    Returns
    -------
    X_train_scaled, X_test_scaled, y_train, y_test, scaler
    """
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Scale features (fit ONLY on training data to prevent data leakage)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)          # apply same transform

    print("=" * 55)
    print("  PREPROCESSING")
    print("=" * 55)
    print(f"  Training samples : {X_train_scaled.shape[0]:,}")
    print(f"  Test samples     : {X_test_scaled.shape[0]:,}")
    print(f"  Features scaled  : Yes (StandardScaler)")
    print()

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


# ── 3. Model Training ─────────────────────────────────────────────────────────

def train_model(X_train, y_train):
    """
    Fit a Linear Regression model on the training data.

    Linear Regression learns coefficients β such that:
        ŷ = β₀ + β₁x₁ + β₂x₂ + … + βₙxₙ
    minimising the sum of squared residuals (OLS).

    Parameters
    ----------
    X_train : scaled training features
    y_train : training targets

    Returns
    -------
    model : fitted LinearRegression instance
    """
    model = LinearRegression()
    model.fit(X_train, y_train)

    print("=" * 55)
    print("  MODEL TRAINING")
    print("=" * 55)
    print("  Algorithm : Linear Regression (OLS)")
    print(f"  Intercept : {model.intercept_:.4f}")
    print()

    return model


# ── 4. Prediction ─────────────────────────────────────────────────────────────

def make_predictions(model, X_test):
    """
    Generate predictions for the test set.

    Parameters
    ----------
    model  : trained LinearRegression model
    X_test : scaled test features

    Returns
    -------
    y_pred : ndarray of predicted house values
    """
    y_pred = model.predict(X_test)
    return y_pred


# ── 5. Evaluation ─────────────────────────────────────────────────────────────

def evaluate_model(y_test, y_pred):
    """
    Compute and display regression evaluation metrics.

    Metrics used
    ------------
    MAE  – Mean Absolute Error   : average magnitude of errors ($100k)
    MSE  – Mean Squared Error    : penalises large errors more heavily
    RMSE – Root MSE              : same units as target (interpretable)
    R²   – Coefficient of determination : proportion of variance explained
           (1.0 = perfect, 0.0 = baseline mean predictor)
    """
    mae  = mean_absolute_error(y_test, y_pred)
    mse  = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2   = r2_score(y_test, y_pred)

    print("=" * 55)
    print("  EVALUATION METRICS")
    print("=" * 55)
    print(f"  MAE  (Mean Absolute Error)      : {mae:.4f}  ($100k)")
    print(f"  MSE  (Mean Squared Error)       : {mse:.4f}")
    print(f"  RMSE (Root Mean Squared Error)  : {rmse:.4f}  ($100k)")
    print(f"  R²   (Coefficient of Det.)      : {r2:.4f}")
    print()
    print("  INTERPRETATION")
    print("  ─────────────────────────────────────────────────")
    print(f"  On average, predictions are off by ~${mae*100_000:,.0f}.")
    print(f"  The model explains {r2*100:.1f}% of the variance in house prices.")
    if r2 >= 0.6:
        print("  ✓ R² ≥ 0.60 – reasonable fit for a linear model.")
    else:
        print("  ✗ R² < 0.60 – consider a non-linear model for better fit.")
    print()

    return {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2}


# ── 6. Visualisation ──────────────────────────────────────────────────────────

def plot_results(y_test, y_pred, feature_names, model):
    """
    Produce two diagnostic plots:
      (a) Actual vs Predicted scatter – shows overall prediction quality.
      (b) Feature importance bar chart – shows each coefficient's magnitude.
    """
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Linear Regression – California Housing", fontsize=14, fontweight="bold")

    # ── Plot A: Actual vs Predicted ──────────────────────────────────────────
    ax = axes[0]
    ax.scatter(y_test, y_pred, alpha=0.3, s=10, color="steelblue", label="Predictions")
    lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
    ax.plot(lims, lims, "r--", linewidth=1.5, label="Perfect fit")
    ax.set_xlabel("Actual Value ($100k)")
    ax.set_ylabel("Predicted Value ($100k)")
    ax.set_title("Actual vs Predicted")
    ax.legend()

    # ── Plot B: Feature Coefficients ─────────────────────────────────────────
    ax2 = axes[1]
    coefs = model.coef_
    colours = ["tomato" if c < 0 else "steelblue" for c in coefs]
    ax2.barh(feature_names, coefs, color=colours)
    ax2.axvline(0, color="black", linewidth=0.8)
    ax2.set_xlabel("Coefficient (standardised units)")
    ax2.set_title("Feature Coefficients")

    plt.tight_layout()
    plt.savefig("ml_results.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("  Plot saved → ml_results.png")
    print()


# ── Main Pipeline ─────────────────────────────────────────────────────────────

def main():
    """
    Orchestrates the full ML pipeline:
    load → preprocess → train → predict → evaluate → visualise.
    """
    print("\n" + "=" * 55)
    print("  MACHINE LEARNING MINI MODEL  –  Linear Regression")
    print("=" * 55 + "\n")

    # Step 1 – Load
    X, y, feature_names = load_data()

    # Step 2 – Preprocess
    X_train, X_test, y_train, y_test, scaler = preprocess_data(X, y)

    # Step 3 – Train
    model = train_model(X_train, y_train)

    # Step 4 – Predict
    y_pred = make_predictions(model, X_test)

    # Step 5 – Evaluate
    metrics = evaluate_model(y_test, y_pred)

    # Step 6 – Visualise
    plot_results(y_test, y_pred, feature_names, model)

    print("Pipeline complete.")


if __name__ == "__main__":
    main()
