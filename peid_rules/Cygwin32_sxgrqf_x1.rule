rule _Cygwin32_sxgrqf
{
	meta:
		description = "Cygwin32"
	strings:
		$a = {5589E583EC04833D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
