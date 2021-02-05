rule _PRO_MIDI_Music_file_wvttaz
{
	meta:
		description = "PRO_MIDI Music file"
	strings:
		$a = {52494646????????524D4944}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
