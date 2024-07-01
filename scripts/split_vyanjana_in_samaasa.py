def send_text_via_clipboard(text):
  try:
    old_clipped_value = clipboard.get_clipboard()
  except:
    old_clipped_value = ""   
  clipboard.fill_clipboard(text)
  keyboard.send_keys("<ctrl>+v")
  # dialog.info_dialog(title="Information", message=text)
  time.sleep(0.2)
  clipboard.fill_clipboard(old_clipped_value)

from importlib.metadata import version
from indic_transliteration import detect, sanscript
time.sleep(0.1)
try:
  text = clipboard.get_selection()
except:
  text = ""
# time.sleep(0.2)
# dialog.info_dialog(title="Information", message=version("indic_transliteration"))
if len(text) == 0:
  send_text_via_clipboard("-")


if len(text) > 0:
  script = detect.detect(text)
  scheme = sanscript.SCHEMES[script]
  if " " in text or '-' in text:
    if hasattr(scheme, "join_post_viraama"):
      text_out = scheme.join_post_viraama(text)

  elif hasattr(scheme, "split_vyanjanas_and_svaras"):
    letters = scheme.split_vyanjanas_and_svaras(text)
    dialog.info_dialog(title="Information", message=",".join(letters))
    if len(text) > 1:
      text_out = scheme.join_strings(letters[:-1]) + "-" + letters[-1]
    elif len(text) == 1:
      text_out = text + scheme["virama"]["्"] + "-" + letters[-1]
    send_text_via_clipboard(text_out)
      
time.sleep(0.2)
clipboard.fill_selection("")
