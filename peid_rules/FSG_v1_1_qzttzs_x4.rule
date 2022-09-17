rule _FSG_v1_1_qzttzs
{
	meta:
		description = "FSG v1_1"
	strings:
		$a = {BBD00140??BF??1040??BE}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
