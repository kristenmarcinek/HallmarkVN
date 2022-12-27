screen gallery():
    tag menu

    imagemap:
        ground "gui/gallery menu.png"
        hover "gui/gallery menu hover.png"
        selected_idle "gui/gallery menu hover.png"

        hotspot (0, 391, 399, 102) action Return()
        hotspot (0, 511, 391, 101) action ShowMenu("load")
        hotspot (0, 631, 400, 105) action ShowMenu("preferences")
        hotspot (0, 753, 397, 102) action Quit(confirm=True)



    imagemap: #tiny monica cg 1 for the gallery

        xpos 50
        ypos 141
        ground Null()
        hover Null()

        if persistent.monica1:
            ground "gui/gallery/monica cg 1 gal.png"
            hover "gui/gallery/monica cg 1 galh.png"

            hotspot (0, 0, 1920, 1080) action ShowMenu ('monica_gallery_1')


    imagemap: #tiny monica cg 2 for the gallery (which doesn't exist yet)

        xpos 50
        ypos 141
        ground Null()
        hover Null()

        if persistent.monica2:
            ground "gui/gallery/monica cg 2 gal.png"
            hover "gui/gallery/monica cg 2 galh.png"

            hotspot (0, 0, 1920, 1080) action ShowMenu ('monica_gallery_2')

    imagemap: #tiny charlie cg 1

        xpos 50
        ypos 141
        ground Null()
        hover Null()

        if persistent.charlie1:
            ground "gui/gallery/charlie cg 1 gal.png"
            hover "gui/gallery/charlie cg 1 galh.png"

            hotspot (0, 0, 1920, 1080) action ShowMenu ('charlie_gallery_1')


    imagemap: #tiny charlie cg 2 (does not exist)

        xpos 50
        ypos 141
        ground Null()
        hover Null()

        if persistent.charlie2:
            ground "gui/gallery/charlie cg 2 gal.png"
            hover "gui/gallery/charlie cg 2 galh.png"

            hotspot (0, 0, 1920, 1080) action ShowMenu ('charlie_gallery_2')


#the big images that show the cg when you click the little gallery buttons

screen monica_gallery_1:
    tag menu
    imagemap:
        ground "/cg/monica cg 1.png"
        hover "/cg/monica cg 1.png"

        hotspot (0, 0, 1920, 1080) action ShowMenu('gallery')

screen monica_gallery_2:
    tag menu
    imagemap:
        ground "/cg/monica cg 2.png"
        hover "/cg/monica cg 2.png"

        hotspot (0, 0, 1920, 1080) action ShowMenu('gallery')

screen charlie_gallery_1:
    tag menu
    imagemap:
        ground "/cg/charlie cg 1.png"
        hover "/cg/charlie cg 1.png"

        hotspot (0, 0, 1920, 1080) action ShowMenu('gallery')

screen charlie_gallery_2:
    tag menu
    imagemap:
        ground "/cg/charlie cg 2.png"
        hover "/cg/charlie cg 2.png"

        hotspot (0, 0, 1920, 1080) action ShowMenu('gallery')
