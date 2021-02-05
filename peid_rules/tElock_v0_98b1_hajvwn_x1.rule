rule _tElock_v0_98b1_hajvwn
{
	meta:
		description = "tElock v0_98b1"
	strings:
		$a = {E925E4FFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
