import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode, DataReturnMode
from st_aggrid.shared import JsCode

import pandas as pd
import pickle
import os
from glob import glob
try:
    import config
except:
    from ntld import config

LOCATIONS = tuple(sorted(config.LOCATIONS))
DATASETS = {
    'customers': 'customers_training.csv',
    'last daily transactions': 'daily_sequence_training.csv',
    'monthly rolling stats': 'rolling_stats.csv',
    'blank periods': 'training_blank_periods.csv'
}

def list_datasets(location):
    location = location.lower().strip()
    path = os.path.join(config.PATH_TO_JOBS, location, 'data', '*.csv')
    files = list(map(lambda x: os.path.basename(x), glob(path)))
    return files

def check_model_availability(location):
    path = os.path.join(config.PATH_TO_JOBS, location, 'models', 'rules_models.pkl')
    return os.path.isfile(path)

def load_dataset(location: str, dataset: str):
    assert location in LOCATIONS
    assert dataset in DATASETS.keys()
    path = os.path.join(config.PATH_TO_JOBS, location, 'data', DATASETS[dataset])
    return pd.read_csv(path)

def aggrid_interactive_table(df: pd.DataFrame):
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()
    options.configure_selection(selection_mode="multiple", use_checkbox=True)
    gridOptions = options.build()
    
    response = AgGrid(
        df,
        gridOptions=gridOptions,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=False,
        reload=True
    )

    # selection = AgGrid(
    #     df,
    #     enable_enterprise_modules=True,
    #     gridOptions=gridOptions,
    #     theme="light",
    #     update_mode=GridUpdateMode.MODEL_CHANGED,
    #     allow_unsafe_jscode=True,
    # )
    

    return response

st.cache(suppress_st_warning=True)
def main():
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">NTLD ML</h1> 
    </div> 
    """

    st.markdown(html_temp, unsafe_allow_html = True)
    Location = st.selectbox('Location', LOCATIONS)
    Dataset = st.selectbox('dataset', tuple(DATASETS.keys()))

    if st.button('LoadData'):
        
        st.write(f"location: {Location}")
        st.write(f"dataset: {Dataset}")
        st.write(f"rules model available: {check_model_availability(Location)}")
        
        data = load_dataset(Location, Dataset)
        response = aggrid_interactive_table(df=data)
        st.subheader("Filtered data will appear below 👇 ")
        st.text("")
        if response:
            df = pd.DataFrame(response["selected_rows"])
            st.table(df)
    

if __name__=='__main__':
    main()