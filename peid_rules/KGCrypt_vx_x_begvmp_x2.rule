rule _KGCrypt_vx_x_begvmp
{
	meta:
		description = "KGCrypt vx_x"
	strings:
		$a = {E8????????5B83EB05EB04524E4421EB02CD20EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
