rule _Microsoft_CAB_SFX_txfruf
{
	meta:
		description = "Microsoft CAB SFX"
	strings:
		$a = {E80A000000E97AFFFFFFCCCCCCCCCC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
