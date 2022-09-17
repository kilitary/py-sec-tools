rule _FixupPak_v1_20_aonmfs
{
	meta:
		description = "FixupPak v1_20"
	strings:
		$a = {558D??????33DB648703E8????????5B8D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
