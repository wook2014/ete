import sys
import random
sys.path.insert(0, "./")
from ete_dev import Tree, TreeStyle, faces
from ete_dev.treeview.main import random_color

def layout(node):
    #node.img_style["size"] = random.randint(5,100)
    node.img_style["hz_line_width"] = 0
    node.img_style["vt_line_width"] = 0
    if node.is_leaf():
        #node.img_style["size"] = random.randint(50, 50)
        f = faces.TextFace("alignedFace", fsize=8, fgcolor="blue")
        #f = faces.AttrFace("name", fsize=random.randint(20,20))
        faces.add_face_to_node(f, node, 0, position="aligned")
        f.border.width = 0
        #f = faces.CircleFace(20, "red")
        #f = faces.AttrFace("name", fsize=20)
        f = faces.TextFace("NAME", fsize=10)
        faces.add_face_to_node(f, node, 0, position="branch-right")
        f.border.width = 0
    #node.img_style["bgcolor"] = random_color()

ts = TreeStyle()
ts.mode = "c"
ts.layout_fn = layout 
ts.show_leaf_name = False
ts.arc_span = 340
ts.arc_start = -70
#ts.allow_face_overlap = True
#ts.show_branch_length = True
ts.draw_guiding_lines = False
ts.optimal_scale_level = "mid"
ts.extra_branch_line_color = "red"

ts.scale = 5
t = Tree()
t.populate(20, random_branches=True, branch_range=(0, 0.7))
t.dist = 0
dists = [n.dist for n in t.traverse() if n.dist != 0]
print max(dists), min(dists)
t.write(outfile="test.nw")
for s in [5, None]:
    ts.scale = s
    t.render("img_scale_%s.png" %s, tree_style = ts, w=600)
t.show(tree_style=ts)


    
        