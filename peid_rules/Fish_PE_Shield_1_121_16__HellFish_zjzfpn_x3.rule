rule _Fish_PE_Shield_1_121_16__HellFish_zjzfpn
{
	meta:
		description = "Fish PE Shield 1_121_16 __ HellFish"
	strings:
		$a = {558BEC83C4D05356578B451083C00C8B008945DC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
