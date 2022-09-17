rule _nBinder_v3_6_1_gmmrhp
{
	meta:
		description = "nBinder v3_6_1"
	strings:
		$a = {6E353634353635333233343534335F6E62335C005C6E353634353635333233343534335F6E62335C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
