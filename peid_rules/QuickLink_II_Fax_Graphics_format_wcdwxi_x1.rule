rule _QuickLink_II_Fax_Graphics_format_wcdwxi
{
	meta:
		description = "QuickLink II Fax Graphics format"
	strings:
		$a = {514C494946415820}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
