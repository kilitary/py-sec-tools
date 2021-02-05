rule _MacroMedia_ShockWave_Movie_file_vmizgf
{
	meta:
		description = "MacroMedia ShockWave Movie file"
	strings:
		$a = {465753}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
