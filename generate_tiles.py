import sys
import json

"""
                <div class="flex-item">
                    <input type="checkbox" id="XXX-toggle" class="toggle-wrapper-toggle">
                    <div class="toggle-wrapper">
                        <div class="toggle-content">
                            <label for="XXX-toggle" class="toggle-content-toggle">
                                <span></span>
                            </label>
                            <p class="checked-content-title">
                                XXX
                            </p>
                            <div class="checked-content-desc">
                                Class: AAAA 000
                                <a href="/assets/media/XXX.pdf" target="_blank" class="button">View File</a>
                                <p>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <label for="XXX-toggle" class="flex-tile" id="XXX">
                    <p class="tile-desc">XXX</p>
                </label>
"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Need 2 parameters")
        exit(1)

    category = sys.argv[1]
    catid = sys.argv[2]

    ret = ""

    with open("assets/media/manifest.json") as f:
        data = json.load(f)

        papers = data[category]
        for paper in papers:
            ret += f"""
                <div class="flex-item">
                    <input type="checkbox" id="{catid}-{paper['id']}-toggle" class="toggle-wrapper-toggle">
                    <div class="toggle-wrapper">
                        <div class="toggle-content">
                            <label for="{catid}-{paper['id']}-toggle" class="toggle-content-toggle">
                                <span></span>
                            </label>
                            <p class="checked-content-title">
                                {paper['title']}
                            </p>
                            <div class="checked-content-desc">
                                Class: {paper['class']}
                                <a href="/assets/media/{category}/{paper['id']}.pdf" target="_blank" class="button">View File</a>
                                <p>
                                    {paper['description']}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <label for="{catid}-{paper['id']}-toggle" class="flex-tile" id="{catid}-{paper['id']}">
                    <p class="tile-desc">{paper['short-title']}</p>
                </label>
"""

    print(ret)