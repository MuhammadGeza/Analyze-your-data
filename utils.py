import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import base64
from scipy.stats import median_abs_deviation, skew, kurtosis, pearsonr

@st.cache
def decode_img(dir_img):
    with open(dir_img, "rb") as image_file:
        byt = base64.b64encode(image_file.read())
    return byt.decode()

def dataset_statistics(df):
    st.markdown(f"""
            <div class="container border border-dark">
                <div class="row">
                    <div class="col-md-6">
                        <table class="table table-hover mt-3">
                                <tr>
                                    <th scope="row">Number of variabels</th>
                                    <td>{len(df.columns)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Number of observations</th>
                                    <td>{len(df)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Missing cells</th>
                                    <td>{sum(df.isna().sum())}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Missing cells (%)</th>
                                    <td>{sum(df.isna().mean()) * 100} %</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="col-md-6">
                        <table class="table table-hover mt-3">
                            <tbody>
                                <tr>
                                    <th scope="row">Duplicate rows</th>
                                    <td>{sum(df.duplicated())}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Duplicate rows (%)</th>
                                    <td>{sum(df.duplicated()) / len(df)} %</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_png = buffer.getvalue()
    graph = base64.b64encode(img_png).decode('utf-8')
    buffer.close()
    return graph


def distplot(df):
    plt.figure(figsize=(2, 5))
    sns.displot(df, height=2.5, kde=True)  
    graph = get_graph()
    return graph

def count_plot(df):
    plt.figure(figsize=(6, 6))
    sns.countplot(df, saturation=1) 
    plt.xticks(rotation=45, ha='right')
    graph = get_graph()
    return graph
    
def tabel(df):
    html = """"""
    d = df.value_counts().to_dict()
    for i, j in d.items():
        html += f"""<tr><td>{i}</td><td>{j}</td><td>{round(j / len(df) * 100, 3)} %</td></tr>"""
    return html

def variabels_overview(df, categorical):
    for i in df.columns:
        try:
            if i not in categorical:
                img = distplot(df[i])
                st.markdown(f"""
                    <div class="container border border-dark">
                        <div class="row">
                            <div class="col-md-12 text-center">
                                <h3 clas="" style="color: #337AB7; font-family: Viga;">{i} <br> <p style="color: black;">Numeric</p></h3>
                            </div>
                        </div>
                        <div class="row border">
                            <div class="col-lg-4 col-md-6">
                                <table class="table mt-3">
                                <tbody>
                                <tr>
                                    <th scope="row">Unique</th>
                                    <td>{df[i].nunique()}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Unique (%)</th>
                                    <td>{round(df[i].nunique() / len(df) * 100, 3)} %</td>
                                </tr>
                                <tr>
                                    <th scope="row">Missing</th>
                                    <td>{sum(df[i].isna())}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Missing (%)</th>
                                    <td>{round(sum(df[i].isna()) / len(df), 3)} %</td>
                                </tr>
                                <tr>
                                    <th scope="row">Zeros</th>
                                    <td>{sum(df[i]==0)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Zeros (%)</th>
                                    <td>{round(sum(df[i]==0) / len(df) * 100, 3)} %</td>
                            </tbody>
                            </table>
                            </div>
                            <div class="col-lg-4 col-md-6conda list">
                            <table class="table table-hover mt-3">
                                <tbody>
                                <tr>
                                    <th scope="row">Mean</th>
                                    <td>{round(df[i].mean(), 3)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Median</th>
                                    <td>{round(df[i].median(), 3)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Minimum</th>
                                    <td>{df[i].min()}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Maximum</th>
                                    <td>{df[i].max()}</td>
                                </tr>
                            </tbody>
                            </table>
                            </div>
                            <div class="col-lg-4 col-md-12">
                                <div class="justify-content-center text-center">
                                    <img src="data:image/png;base64,{img}">
                                </div>
                            </div>
                            </div>
                            <div class="row mt-2">
                            <div class="col-md-6 mb-2">
                                <p class="h4 text-center">Quantile statistics</p>
                                <table class="table table-hover">
                                <tbody>
                                <tr>
                                    <th scope="row">Minimum</th>
                                    <td>{df[i].min()}</td>
                                </tr>
                                <tr>
                                    <th scope="row">5-th percentile</th>
                                    <td>{round(df[i].quantile(.05),4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Q1</th>
                                    <td>{round(df[i].quantile(.25),4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Median</th>
                                    <td>{round(df[i].quantile(.5), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Q3</th>
                                    <td>{round(df[i].quantile(.75),4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">95-th percentile</th>
                                    <td>{round(df[i].quantile(.95),4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Interquartile range (IQR)</th>
                                    <td>{round(df[i].quantile(.75) - df[i].quantile(.25), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Maximum</th>
                                    <td>{df[i].max()}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Range</th>
                                    <td>{df[i].max() - df[i].min()}</td>
                                </tr>
                            </tbody>
                            </table>
                            </div>
                            <div class="col-md-6 mb-2">
                            <p class="h4 text-center">Descriptive statistics</p>
                                <table class="table table-hover">
                                <tbody>
                                <tr>
                                    <th scope="row">Variance</th>
                                    <td>{round(df[i].var(), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Standard deviation</th>
                                    <td>{round(df[i].std(), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Coefficient of variation (CV)</th>
                                    <td>{round(df[i].std() / df[i].mean() * 100, 4)} %</td>
                                </tr>
                                <tr>
                                    <th scope="row">Mean</th>
                                    <td>{round(df[i].mean(), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Median Absolute Deviation (MAD)	</th>
                                    <td>{round(median_abs_deviation(df[i]), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Mean Absolute Deviation (MAD)	</th>
                                    <td>{round(df[i].mad(), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Skewness</th>
                                    <td>{round(skew(df[i]), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Kurtosis</th>
                                    <td>{round(kurtosis(df[i]), 4)}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Sum</th>
                                    <td>{round(df[i].sum(), 4)}</td>
                                </tr>
                            </tbody>
                            </table>
                            </div>
                            </div>
                        </div>
                    </div>""", unsafe_allow_html=True)
            else:
                img = count_plot(df[i])
                st.markdown(f"""
                    <div class="container border border-dark">
                        <div class="row">
                            <div class="col-md-12 text-center">
                                <h3 style="color: #337AB7; font-family: Viga;">{i} <br> <p style="color: black;">Categoric</p></h3>
                            </div>
                        </div>
                        <div class="row border">
                            <div class="col-lg-8">
                                <table class="table mt-3">
                                <tbody>
                                <tr>
                                    <th scope="row">Count</th>
                                    <td>{df[i].count()}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Unique</th>
                                    <td>{df[i].nunique()}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Unique (%)</th>
                                    <td>{round(df[i].nunique() / len(df) * 100, 3)} %</td>
                                </tr>
                                <tr>
                                    <th scope="row">Missing</th>
                                    <td>{sum(df[i].isna())}</td>
                                </tr>
                                <tr>
                                    <th scope="row">Missing (%)</th>
                                    <td>{round(sum(df[i].isna()) / len(df), 3)} %</td>
                                </tr>
                            </tbody>
                            </table>
                            </div>
                            <div class="col-lg-3">
                                <div class="justify-content-center text-center">
                                    <img style="width: 270px; height: 250px;" src="data:image/png;base64,{img}">
                                </div>
                            </div>
                            </div>
                            <div class="row mt-2 justify-content-center">
                            <div class="col-md-8">
                                <table class="table mt-3">
                                <tbody>
                                    <p class="h4 text-center">Common values</p>
                                    <tr>
                                        <th scope="row">Value</th>
                                        <th scope="row">Count</th>
                                        <th scope="row">Frequency</th>
                                    </tr>
                                    <div>{tabel(df[i])}</div>
                                </tbody>
                                </table>
                            </div>
                            </div>
                        </div>
                    </div>""", unsafe_allow_html=True)
        except:
            st.warning(f"**{i}** has a categorical data type, please select **{i}**  in the categorical options above")

def scatter(df, x, y):
    fig = plt.figure(figsize=(9, 4.5))
    plt.title(f'Correlation value (pearson): {pearsonr(df[x], df[y])[0]}')
    sns.scatterplot(x=x, y=y, data=df)
    graph = get_graph()
    return graph

def interactions(df):
    col1, col2 = st.columns(2)
    with col1:
        col1 = st.selectbox('X axis', df.columns)
    with col2:
        col2 = st.selectbox('Y axis', df.columns[::-1])

    image = scatter(df, col1, col2)
    st.markdown(f"""<div class="container border border-dark">
                    <div class="row text-center">
                        <div class="col-md-12 mb-3">
                            <img class="responsive" style="width: 100; height: 100;" src="data:image/png;base64,{image}">
                        </div>
                    </div>
                    </div>""", unsafe_allow_html=True)

def heatmap_plot(df, method):
    color = {
        'pearson': 'Greens',
        'kendall': 'Blues',
        'spearman': 'Purples'
    }
    plt.figure(figsize=(7, 6))
    sns.heatmap(df.corr(method=method), cmap=color[method], vmin=-1, vmax=1, linewidths=0.1, square=True)
    plt.xticks(rotation=45, ha='right')
    graph = get_graph()
    return graph
    
def correlations(df):
    attr = {
        'pearson': "<h3>Pearson's r</h3>The Pearson's correlation coefficient (<em>r</em>) is a measure of linear correlation between two variables. It's value lies between -1 and +1, -1 indicating total negative linear correlation, 0 indicating no linear correlation and 1 indicating total positive linear correlation. Furthermore, <em>r</em> is invariant under separate changes in location and scale of the two variables, implying that for a linear function the angle to the x-axis does not affect <em>r</em>.<br><br>To calculate <em>r</em> for two variables <em>X</em> and <em>Y</em>, one divides the covariance of <em>X</em> and <em>Y</em> by the product of their standard deviations.",
        'kendall': "<h3>Kendall's τ</h3>Similarly to Spearman's rank correlation coefficient, the Kendall rank correlation coefficient (<em>τ</em>) measures ordinal association between two variables. It's value lies between -1 and +1, -1 indicating total negative correlation, 0 indicating no correlation and 1 indicating total positive correlation. <br><br>To calculate <em>τ</em> for two variables <em>X</em> and <em>Y</em>, one determines the number of concordant and discordant pairs of observations. <em>τ</em> is given by the number of concordant pairs minus the discordant pairs divided by the total number of pairs.",
        'spearman':"<h3>Spearman's ρ</h3>The Spearman's rank correlation coefficient (<em>ρ</em>) is a measure of monotonic correlation between two variables, and is therefore better in catching nonlinear monotonic correlations than Pearson's <em>r</em>. It's value lies between -1 and +1, -1 indicating total negative monotonic correlation, 0 indicating no monotonic correlation and 1 indicating total positive monotonic correlation.<br><br>To calculate <em>ρ</em> for two variables <em>X</em> and <em>Y</em>, one divides the covariance of the rank variables of <em>X</em> and <em>Y</em> by the product of their standard deviations."
    }
    method = st.selectbox('Choose method',['pearson', 'kendall', 'spearman'])
    image = heatmap_plot(df, method)
    st.markdown(f"""<div class="container border border-dark">
                    <div class="row">
                        <div class="col-md-8 mb-3 text-center">
                            <img class="responsive" src="data:image/png;base64,{image}">
                        </div>
                        <div class="col-md-4 mb-3">
                            {attr[method]}
                        </div>
                    </div>
                    </div>""", unsafe_allow_html=True)