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

from indic_transliteration import detect, sanscript
import regex
try:
  text = clipboard.get_selection()
except:
  text = ""
text_out = None
if len(text) > 0:
  if regex.fullmatch("[\d-]+", text):
    # Markdown footnote
    text_out = f"[^{text}]"
  elif regex.fullmatch("[\d-]+[\.:]", text):
    # Markdown footnote
    text_out = f"[^{text[:-1]}]:"
  else:
      script = detect.detect(text)
      scheme = sanscript.SCHEMES[script]
      if " " in text or '-' in text:
        if hasattr(scheme, "join_post_viraama"):
          text_out = scheme.join_post_viraama(text)

      elif hasattr(scheme, "split_vyanjanas_and_svaras"):
          final_svara = scheme.split_vyanjanas_and_svaras(text)[-1]
          if len(text) > 1:
            text_out = text[:-1] + scheme["virama"]["्"] + " " + final_svara
          elif len(text) == 1:
            text_out = text + scheme["virama"]["्"] + " " + final_svara
          # dialog.info_dialog(title="Information", message=text_out)

if text_out is not None:
  send_text_via_clipboard(text_out)

clipboard.fill_selection("")
