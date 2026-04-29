import re

html_content = '''
                        <div class="accordion" id="usgScansAccordion">
                            <!-- Category 1 -->
                            <div class="accordion-item" style="margin-bottom: 15px; border: none; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                                <h2 class="accordion-header" id="headingOne">
                                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" style="font-weight: 700; color: #1a1a1a; background-color: #fff; border-radius: 10px; padding: 20px;">
                                        ABDOMEN
                                    </button>
                                </h2>
                                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#usgScansAccordion">
                                    <div class="accordion-body" style="padding: 0;">
                                        <table class="table table-striped table-hover mb-0">
                                            <thead>
                                                <tr><th style="padding: 15px 20px;">Test Name</th><th style="padding: 15px 20px; text-align: right;">Price (₹)</th></tr>
                                            </thead>
                                            <tbody>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND MALE ABDOMEN</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1400</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND FEMALE ABDOMEN</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1400</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND KUB</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1500</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND WHOLE ABDOMEN</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND ABDOMEN + PVR</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1400+300</td></tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                            <!-- Category 2 -->
                            <div class="accordion-item" style="margin-bottom: 15px; border: none; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                                <h2 class="accordion-header" id="headingTwo">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo" style="font-weight: 700; color: #1a1a1a; background-color: #fff; border-radius: 10px; padding: 20px;">
                                        PELVIS
                                    </button>
                                </h2>
                                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#usgScansAccordion">
                                    <div class="accordion-body" style="padding: 0;">
                                        <table class="table table-striped table-hover mb-0">
                                            <thead>
                                                <tr><th style="padding: 15px 20px;">Test Name</th><th style="padding: 15px 20px; text-align: right;">Price (₹)</th></tr>
                                            </thead>
                                            <tbody>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND PELVIS</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND ABD &amp; PELVIS</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND ABD &amp; PELVIS + AFC</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2300</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND OF EARLY PREGNANCY</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                            <!-- Category 3 -->
                            <div class="accordion-item" style="margin-bottom: 15px; border: none; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                                <h2 class="accordion-header" id="headingThree">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree" style="font-weight: 700; color: #1a1a1a; background-color: #fff; border-radius: 10px; padding: 20px;">
                                        TIFFA
                                    </button>
                                </h2>
                                <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#usgScansAccordion">
                                    <div class="accordion-body" style="padding: 0;">
                                        <table class="table table-striped table-hover mb-0">
                                            <thead>
                                                <tr><th style="padding: 15px 20px;">Test Name</th><th style="padding: 15px 20px; text-align: right;">Price (₹)</th></tr>
                                            </thead>
                                            <tbody>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND NT + EARLY TIFFA</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2300</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND NT (3D)</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2700</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND OBST + TIFFA</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2300</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND TIFFA 3D &amp; 4D</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">3500</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND N.T</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2300</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND OBSTETRICS</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                            <!-- Category 4 -->
                            <div class="accordion-item" style="margin-bottom: 15px; border: none; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                                <h2 class="accordion-header" id="headingFour">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour" style="font-weight: 700; color: #1a1a1a; background-color: #fff; border-radius: 10px; padding: 20px;">
                                        DOPPLERS
                                    </button>
                                </h2>
                                <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#usgScansAccordion">
                                    <div class="accordion-body" style="padding: 0;">
                                        <table class="table table-striped table-hover mb-0">
                                            <thead>
                                                <tr><th style="padding: 15px 20px;">Test Name</th><th style="padding: 15px 20px; text-align: right;">Price (₹)</th></tr>
                                            </thead>
                                            <tbody>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND OBST + DOPPLER</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2300</td></tr>
                                                <tr><td style="padding: 15px 20px;">VENOUS DOPPLER SINGLE LIMB (ANY)</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2300</td></tr>
                                                <tr><td style="padding: 15px 20px;">ARTERIAL DOPPLER SINGLE LIMB (ANY)</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2300</td></tr>
                                                <tr><td style="padding: 15px 20px;">CAROTID DOPPLER</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2500</td></tr>
                                                <tr><td style="padding: 15px 20px;">SCROTUM DOPPLER</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2400</td></tr>
                                                <tr><td style="padding: 15px 20px;">2D ECHO- CARDIOLOGY</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2400</td></tr>
                                                <tr><td style="padding: 15px 20px;">ECG</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">400</td></tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                            <!-- Category 5 -->
                            <div class="accordion-item" style="margin-bottom: 15px; border: none; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                                <h2 class="accordion-header" id="headingFive">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFive" aria-expanded="false" aria-controls="collapseFive" style="font-weight: 700; color: #1a1a1a; background-color: #fff; border-radius: 10px; padding: 20px;">
                                        MAMMOGRAPHY &amp; USG SONO MAMMO
                                    </button>
                                </h2>
                                <div id="collapseFive" class="accordion-collapse collapse" aria-labelledby="headingFive" data-bs-parent="#usgScansAccordion">
                                    <div class="accordion-body" style="padding: 0;">
                                        <table class="table table-striped table-hover mb-0">
                                            <thead>
                                                <tr><th style="padding: 15px 20px;">Test Name</th><th style="padding: 15px 20px; text-align: right;">Price (₹)</th></tr>
                                            </thead>
                                            <tbody>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND SINGLE BREAST</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1600</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND BOTH BREASTS</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">3000</td></tr>
                                                <tr><td style="padding: 15px 20px;">X-RAY MAMMOGRAPHY SINGLE BREAST</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1600</td></tr>
                                                <tr><td style="padding: 15px 20px;">X-RAY MAMMOGRAPHY BOTH BREASTS</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">3000</td></tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                            <!-- Category 6 -->
                            <div class="accordion-item" style="margin-bottom: 15px; border: none; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                                <h2 class="accordion-header" id="headingSix">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSix" aria-expanded="false" aria-controls="collapseSix" style="font-weight: 700; color: #1a1a1a; background-color: #fff; border-radius: 10px; padding: 20px;">
                                        SPECIAL SCANS
                                    </button>
                                </h2>
                                <div id="collapseSix" class="accordion-collapse collapse" aria-labelledby="headingSix" data-bs-parent="#usgScansAccordion">
                                    <div class="accordion-body" style="padding: 0;">
                                        <table class="table table-striped table-hover mb-0">
                                            <thead>
                                                <tr><th style="padding: 15px 20px;">Test Name</th><th style="padding: 15px 20px; text-align: right;">Price (₹)</th></tr>
                                            </thead>
                                            <tbody>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND SCROTUM DOPPLER</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2400</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND NECK</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">NEURO SONOGRAPHY (NSG)</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND THYROID</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND FETAL 2D ECHO</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">3500</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND SOFT TISSUE</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">FOLLICULAR STUDIES (3 VISITS)</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">2400</td></tr>
                                                <tr><td style="padding: 15px 20px;">FOLLICULAR STUDIES 4TH EXTRA VISIT</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">800</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND OF RENAL DOPPLER</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">3500</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND OF SPECIAL PARTS</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND TWINS</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1200</td></tr>
                                                <tr><td style="padding: 15px 20px;">FOLLICULAR STUDIES FIRST VISIT</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                                <tr><td style="padding: 15px 20px;">FOLLICULAR STUDIES 2ND VISIT-SAME CYCLE</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">600</td></tr>
                                                <tr><td style="padding: 15px 20px;">FOLLICULAR STUDIES 3RD VISIT-SAME CYCLE</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">600</td></tr>
                                                <tr><td style="padding: 15px 20px;">ULTRASOUND OF GRAVID ABDOMEN</td><td style="padding: 15px 20px; text-align: right; font-weight: 600;">1800</td></tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                        </div>
'''

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old usgScansAccordion
# find the start and end of it.
import re
start_marker = '<div class="accordion" id="usgScansAccordion">'
# we need to find where the <div class="accordion" id="usgScansAccordion"> ends.
# The structure ends right before "<!-- CT Scans Accordion starts here -->" which I just added!
end_marker = '<!-- CT Scans Accordion starts here -->'
if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    # Actually it ends at </div> \n </div><!-- /.col-lg-8 --> 
    # But it's easier to use regex or find to replace everything from start_marker to the last </div> before end_marker.
    
    # We can just construct a pattern to match everything between <div class="accordion" id="usgScansAccordion"> and \s*</div>\s*<!-- CT Scans Accordion starts here -->
    pattern = re.compile(r'<div class="accordion" id="usgScansAccordion">.*?</div>\s*</div><!-- /.col-lg-8 -->\s*<!-- CT Scans Accordion starts here -->', re.DOTALL)
    
    new_block = html_content + '\n                    </div><!-- /.col-lg-8 -->\n\n                        <!-- CT Scans Accordion starts here -->'
    
    new_content = pattern.sub(new_block, content)
    
    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced USG Scans list with prices.")
else:
    print("Failed to find markers")
