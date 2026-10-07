%pip install ipywidgets

import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output

# 1. clock time per day
s_times = ["08:00","09:30","10:00","10:30","11:00","11:30","12:00"]

violation_dropdown = widgets.Dropdown(options=["No", "Yes"],value="No",description="Violation:")
