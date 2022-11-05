from indic_transliteration import detect, sanscript
text = clipboard.get_selection()
time.sleep(0.1)
dialog.info_dialog(title="Information", message=text)
if len(text) == 0:
  keyboard.send_keys("-")

if len(text) > 0:
  script = detect.detect(text)
  scheme = sanscript.SCHEMES[script]
  final_svara = scheme.split_vyanjanas_and_svaras(text)[-1]
  if len(text) > 1:
    text_out = text[:-1] + scheme["virama"]["्"] + "-" + final_svara
  elif len(text) == 1:
    text_out = text + scheme["virama"]["्"] + "-" + final_svara
  # dialog.info_dialog(title="Information", message=text_out)
  old_clipped_value = clipboard.get_clipboard()
  clipboard.fill_clipboard(text_out)
  keyboard.send_keys("<ctrl>+v")
  time.sleep(0.1)
  clipboard.fill_clipboard(old_clipped_value)
  clipboard.fill_selection("")
