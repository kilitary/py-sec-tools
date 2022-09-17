rule _E_language_wapffb
{
	meta:
		description = "E language"
	strings:
		$a = {E80600000050E8??010000558BEC81C4F0FEFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
