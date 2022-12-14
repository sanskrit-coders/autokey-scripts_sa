def send_text_via_clipboard(text):
    old_clipped_value = clipboard.get_clipboard()
    clipboard.fill_clipboard(text)
    keyboard.send_keys("<ctrl>+v")
    # dialog.info_dialog(title="Information", message=text)
    time.sleep(0.2)
    clipboard.fill_clipboard(old_clipped_value)

from indic_transliteration import detect, sanscript
text = clipboard.get_selection()
time.sleep(0.1)
# dialog.info_dialog(title="Information", message=text)
if len(text) == 0:
  send_text_via_clipboard("-")


if len(text) > 0:
  script = detect.detect(text)
  scheme = sanscript.SCHEMES[script]
  if hasattr(scheme, "split_vyanjanas_and_svaras"):
      final_svara = scheme.split_vyanjanas_and_svaras(text)[-1]
      if len(text) > 1:
        text_out = text[:-1] + scheme["virama"]["्"] + "-" + final_svara
      elif len(text) == 1:
        text_out = text + scheme["virama"]["्"] + "-" + final_svara
      # dialog.info_dialog(title="Information", message=text_out)
      send_text_via_clipboard(text_out)
      
time.sleep(0.2)
clipboard.fill_selection("")
