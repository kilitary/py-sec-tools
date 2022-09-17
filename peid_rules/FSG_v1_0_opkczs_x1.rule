rule _FSG_v1_0_opkczs
{
	meta:
		description = "FSG v1_0"
	strings:
		$a = {BBD0014000BF00104000BE????????53E80A00000002D275058A164612D2C3FCB280A46A025B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
