from indic_transliteration import detect, sanscript
import regex
text = clipboard.get_selection()
text_out = None
if len(text) > 0:
  if regex.fullmatch("\d+", text):
    # Markdown footnote
    text_out = f"[^{text}]"
  elif regex.fullmatch("\d+[\.:]", text):
    # Markdown footnote
    text_out = f"[^{text[:-1]}]:"
  else:
      script = detect.detect(text)
      scheme = sanscript.SCHEMES[script]
      if hasattr(scheme, "split_vyanjanas_and_svaras"):
          final_svara = scheme.split_vyanjanas_and_svaras(text)[-1]
          if len(text) > 1:
            text_out = text[:-1] + scheme["virama"]["्"] + " " + final_svara
          elif len(text) == 1:
            text_out = text + scheme["virama"]["्"] + " " + final_svara
          # dialog.info_dialog(title="Information", message=text_out)

if text_out is not None:
  old_clipped_value = clipboard.get_clipboard()
  clipboard.fill_clipboard(text_out)
  keyboard.send_keys("<ctrl>+v")
  time.sleep(0.1)
  clipboard.fill_clipboard(old_clipped_value)
clipboard.fill_selection("")
