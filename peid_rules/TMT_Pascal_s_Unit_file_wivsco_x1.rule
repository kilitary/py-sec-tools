rule _TMT_Pascal_s_Unit_file_wivsco
{
	meta:
		description = "TMT_Pascal_s Unit file"
	strings:
		$a = {5000000053504650}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
