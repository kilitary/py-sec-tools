rule _EP_v2_0_zttoyo
{
	meta:
		description = "EP v2_0"
	strings:
		$a = {6A??60E90101}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
