import View.View
import Model.FileHandler


work = True
while work:
   ask = View.View.user_input()
   if ask == 1:
        data = View.add()
        Model.FileHandler.add(data)
        # elif ask == 2:
        #     xx = view.search()
        #     database.rename(xx)
        # elif ask == 3:
        #     vv = view.search()
        #     database.delete(vv)
        # elif ask == 4:
        #     ss = view.search()
        #     database.sr(ss)
        # elif ask == 5:
        #     database.sort_name()
        # elif ask == 6:
        #     View.finish()
        

