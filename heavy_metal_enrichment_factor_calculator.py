CRUSTAL_AVERAGES = {
    "Pb": 15.0,
    "Cd": 0.1,
    "Hg": 0.08,
    "As": 1.8,
    "Cu": 55.0,
    "Zn": 70.0,
    "Cr": 100.0,
    "Ni": 75.0,
}

def compute_enrichment_factor(c_sample: float, c_bg: float) -> float:
    """Return the enrichment factor EF = C_sample / C_bg."""
    if c_bg <= 0:
        raise ValueError("Background concentration must be positive.")
    return c_sample / c_bg

def classify_enrichment(ef: float):
    """Return (classification_string, hex_color) based on EF thresholds."""
    if ef < 1:
        return "No enrichment", "#2e7d32"          # dark green
    elif ef < 3:
        return "Minor enrichment", "#66bb6a"        # green
    elif ef < 5:
        return "Moderate enrichment", "#fbc02d"     # yellow
    elif ef < 10:
        return "Moderately severe enrichment", "#f57c00"  # orange
    elif ef < 25:
        return "Severe enrichment", "#d84315"       # deep orange
    else:
        return "Very severe enrichment", "#b71c1c"  # dark red

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def create_ef_plot(ef: float):
    """Create a horizontal bar plot of EF with class boundary markers."""
    fig, ax = plt.subplots(figsize=(6, 1.8))
    xmax = max(30, ef + 5)

    # Draw colored regions for each class
    boundaries = [0, 1, 3, 5, 10, 25, xmax]
    colors = ["#2e7d32", "#66bb6a", "#fbc02d", "#f57c00", "#d84315", "#b71c1c"]
    labels = ["None", "Minor", "Moderate", "Mod. severe", "Severe", "Very severe"]
    for i in range(len(boundaries)-1):
        left = boundaries[i]
        right = boundaries[i+1]
        ax.axvspan(left, right, color=colors[i], alpha=0.3, zorder=0)

    # Plot the bar for EF
    bar_color = "#1565c0"
    ax.barh(0, ef, height=0.6, color=bar_color, edgecolor="black", zorder=3)

    # Boundary markers
    for b in boundaries[:-1]:
        ax.axvline(b, color="grey", linestyle="--", linewidth=0.5)

    # Labels and ticks
    ax.set_xlim(0, xmax)
    ax.set_ylim(-0.5, 0.5)
    ax.set_yticks([])
    ax.set_xlabel("Enrichment Factor")
    ax.set_title(f"EF = {ef:.2f}", fontsize=12, weight="bold")

    # Legend for classes
    patches = [mpatches.Patch(color=c, alpha=0.3, label=l) for c, l in zip(colors, labels)]
    ax.legend(handles=patches, loc="upper right", fontsize=6, framealpha=1)

    plt.tight_layout()
    return fig
