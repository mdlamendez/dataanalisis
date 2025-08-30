from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]

RESULT_DIR = ROOT_DIR / "results" # 
PLOTS_DIR = RESULT_DIR / "plots"
HISTOGRAM_DIR = PLOTS_DIR / "histograms"
BOXPLOT_DIR = PLOTS_DIR / "boxplots"
SCATTER_DIR = PLOTS_DIR / "scatters"
HEATMAP_DIR = PLOTS_DIR / "heatmaps"
REGRESSION_DIR = PLOTS_DIR / "regression"


DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


