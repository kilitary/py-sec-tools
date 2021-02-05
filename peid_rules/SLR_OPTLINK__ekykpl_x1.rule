rule _SLR_OPTLINK__ekykpl
{
	meta:
		description = "SLR _OPTLINK_"
	strings:
		$a = {BF????8EDFFA8ED781C4????FBB430CD21}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
