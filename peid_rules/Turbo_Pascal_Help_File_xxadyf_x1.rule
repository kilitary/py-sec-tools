rule _Turbo_Pascal_Help_File_xxadyf
{
	meta:
		description = "Turbo Pascal Help File"
	strings:
		$a = {545552??????504153????????48454C50}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
