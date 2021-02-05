rule _Microsoft_WAV_Audio_file_ujvrop
{
	meta:
		description = "Microsoft WAV Audio file"
	strings:
		$a = {52494646????????57415645666D74}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
