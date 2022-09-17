rule _FSG_v1_1_uezhhk
{
	meta:
		description = "FSG v1_1"
	strings:
		$a = {EB01??EB02??????80????00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
