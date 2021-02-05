rule _MicroJoiner_1_1__coban2k_uexwcg
{
	meta:
		description = "MicroJoiner 1_1 __ coban2k"
	strings:
		$a = {BE0C704000BBF811400033ED83EE04392E7411}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
