rule _FSG_v1_1_lknezo
{
	meta:
		description = "FSG v1_1"
	strings:
		$a = {BBD00140??BF??1040??BE????????FCB2808A064688074702D275058A16}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
