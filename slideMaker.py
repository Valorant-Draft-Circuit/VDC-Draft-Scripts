from dataStructurePullerThingy import populateFranchises, tierPulls, franchises, picks
from pptx import Presentation
from pptx.util import Inches

def makeSlides():
    prs = Presentation()
    prs.slide_width = Inches(16)
    prs.slide_height = Inches(9)
    slide_layout = prs.slide_layouts[0]
    populateFranchises("VDCContracts-Teams.csv")
    for tier in picks.keys():
        tierPulls("Season1VDCDraft_Board-Bot_CommandOutput.csv", tier)
        title = prs.slides.add_slide(slide_layout)
        title.shapes.title.text = tier + " draft starts now"
        for pick in picks[tier].keys():
                slide = prs.slides.add_slide(slide_layout)
                slide.placeholders[1].text = str(tier) + ": Round " + str(picks[tier][pick]['Round']) + ", Pick " + str(picks[tier][pick]['Pick']) + "\nFranchise: " + str(franchises[picks[tier][pick]["GM"]]['Franchise']) + "\nTeam: " + str(franchises[picks[tier][pick]["GM"]][tier])
                slide.shapes.title.text = picks[tier][pick]["Player Selected"]
    
    prs.save('vdcDraft_widescreen.pptx')
    print("Done")
    return None
makeSlides()