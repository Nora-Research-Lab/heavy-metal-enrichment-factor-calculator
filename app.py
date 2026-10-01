import gradio as gr
from heavy_metal_enrichment_factor_calculator import (
    CRUSTAL_AVERAGES,
    compute_enrichment_factor,
    classify_enrichment,
    create_ef_plot,
)

def update_background(element):
    if element == "Other":
        return gr.update(value=None, interactive=True)
    return gr.update(value=CRUSTAL_AVERAGES.get(element, 0.0), interactive=True)

def calculate(sample_conc, bg_conc, element):
    if element == "Other" and (bg_conc is None or bg_conc <= 0):
        return None, None, "Please provide a valid background concentration for 'Other'.", None
    if sample_conc is None or sample_conc <= 0:
        return None, None, "Sample concentration must be positive.", None
    if bg_conc is None or bg_conc <= 0:
        return None, None, "Background concentration must be positive.", None
    ef = compute_enrichment_factor(sample_conc, bg_conc)
    classification, color = classify_enrichment(ef)
    fig = create_ef_plot(ef)
    ef_display = f"{ef:.2f}"
    badge_html = f'<span style="background-color:{color}; color:white; padding:6px 12px; border-radius:4px; font-weight:bold;">{classification}</span>'
    return ef_display, badge_html, None, fig

with gr.Blocks(title="Heavy Metal Enrichment Factor Calculator", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Heavy Metal Enrichment Factor (EF) Calculator
        Compute the enrichment factor for a heavy metal in a sample relative to its crustal average.
        Select an element to auto-fill the background concentration, or choose 'Other' to enter manually.
        """
    )
    with gr.Row():
        with gr.Column(scale=1):
            element_dropdown = gr.Dropdown(
                choices=["Pb", "Cd", "Hg", "As", "Cu", "Zn", "Cr", "Ni", "Other"],
                label="Select Heavy Metal Element",
                value="Pb",
            )
            with gr.Row():
                sample_input = gr.Number(label="Metal concentration in sample (mg/kg)", value=1.0, minimum=0)
                bg_input = gr.Number(
                    label="Background/Reference concentration (mg/kg)",
                    value=CRUSTAL_AVERAGES["Pb"],
                    minimum=0,
                )
            calc_btn = gr.Button("Calculate", variant="primary", scale=0)
            error_box = gr.Markdown(visible=False)
        with gr.Column(scale=1):
            with gr.Row():
                ef_display = gr.Markdown(label="Enrichment Factor", value="")
                class_badge = gr.HTML(label="Classification")
            plot_output = gr.Plot(label="Enrichment Factor Plot")

    element_dropdown.change(
        fn=update_background,
        inputs=element_dropdown,
        outputs=bg_input,
    )

    calc_btn.click(
        fn=calculate,
        inputs=[sample_input, bg_input, element_dropdown],
        outputs=[ef_display, class_badge, error_box, plot_output],
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
