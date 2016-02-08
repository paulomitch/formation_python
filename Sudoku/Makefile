
UI = gui_ui.py cell_ui.py

dep : $(UI)# gui_rc.py

run : dep
	./example.py

%_ui.py : %_ui.ui
	@echo "compiling $<"
	pyuic5 $< > $@

#gui_rc.py : gui.qrc icons/*
#	pyrcc5 gui.qrc > gui_rc.py
