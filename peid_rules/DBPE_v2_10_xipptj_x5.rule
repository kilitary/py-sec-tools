rule _DBPE_v2_10_xipptj
{
	meta:
		description = "DBPE v2_10"
	strings:
		$a = {9C60E8CA??????03??04??05??06??07??08}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
