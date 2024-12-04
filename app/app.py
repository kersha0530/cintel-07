
# Define imports
import seaborn as sns
from faicons import icon_svg
from shiny import reactive
from shiny.express import input, render, ui
import palmerpenguins
from shinyswatch import theme  # Import shinyswatch to use bootswatch themes

# Load the penguins dataset
df = palmerpenguins.load_penguins()

# Page Title with Cyborg theme
# Define page options: Includes title and sets the app as fillable
ui.page_opts(title="Penguins dashboard", fillable=True, theme=theme.cyborg)

# Sidebar with filter controls and helpful links
with ui.sidebar(title="Filter controls"):

    # Slider input for filtering penguins by mass
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)

    # Checkbox group for selecting species of penguins to include
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )

    # Horizontal rule for separating sections
    ui.hr()

    # Helpful links
    ui.h6("Links")
    ui.a("GitHub Source", href="https://github.com/kersha0530/cintel-07-tdash", target="_blank")
    ui.a("GitHub Issues", href="https://github.com/kersha0530/cintel-07-tdash/issues", target="_blank")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a("Template: Basic Dashboard", href="https://shiny.posit.co/py/templates/dashboard/", target="_blank")

# Main section with value boxes and scatterplot visualization
with ui.layout_column_wrap(fill=False):

    # Value box for displaying the total number of penguins
    with ui.value_box(showcase=icon_svg("earlybirds"), style="color:#56cc9d;"):
        "Number of penguins"

        @render.text
        def count():
            return filtered_df().shape[0]

    # Value box for displaying the average bill length of the filtered penguins
    with ui.value_box(showcase=icon_svg("ruler-horizontal"), style="color: #fd7e14;"):
        "Average bill length"

        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"

    # Value box for displaying the average bill depth of the filtered penguins
    with ui.value_box(showcase=icon_svg("ruler-vertical"), style="color: #007bff;"):
        "Average bill depth"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"

with ui.layout_columns():

    # Main visualizations: Scatterplot and Interactive DataGrid
    # Scatterplot for bill length vs. bill depth
    with ui.card(full_screen=True):
        ui.card_header(
            "Bill length and depth",
            style="font-weight: bold; color: #56cc9d;",
        )

        @render.plot
        def length_depth():
            return sns.scatterplot(
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species",
            )

    # Filtered DataGrid based on selected species
    
    with ui.card(full_screen=True):
        ui.card_header(
            "Penguin data",
            style="font-weight: bold; color: #56cc9d;",
        )

        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)

# Reactive function to filter the data based on user inputs
# Filter penguins based on selected species
# Further filter by body mass
@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df

