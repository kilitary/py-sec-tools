rule _Sierra_s_audio_file_aesdfi
{
	meta:
		description = "Sierra_s audio file"
	strings:
		$a = {8D0C534F4C0022560D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
