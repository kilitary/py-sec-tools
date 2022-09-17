rule _UnderGround_Crypter__by_Booster2000_yfvngr
{
	meta:
		description = "UnderGround Crypter _ by Booster2000"
	strings:
		$a = {558BEC83C4F0B8743C0011E894F9FFFFE8BFFEFFFFE80AF3FFFF8BC0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
