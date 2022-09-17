rule _FSG_v1_3_zzbrie
{
	meta:
		description = "FSG v1_3"
	strings:
		$a = {BBD0014000BF00104000BE????????53BB????????B280A4B680FFD373F933C9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
