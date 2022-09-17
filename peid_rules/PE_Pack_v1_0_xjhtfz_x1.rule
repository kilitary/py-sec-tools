rule _PE_Pack_v1_0_xjhtfz
{
	meta:
		description = "PE Pack v1_0"
	strings:
		$a = {74??E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
