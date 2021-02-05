rule _MIDI_Music_file_ouyfsg
{
	meta:
		description = "MIDI Music file"
	strings:
		$a = {4D54686400000006????????????4D54}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
