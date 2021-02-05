rule _RLPack_1_19_Basic_Edition_jxzfiv
{
	meta:
		description = "RLPack 1_19 Basic Edition"
	strings:
		$a = {60E8000000008B2C2483C404837C242801750C8B4424248985????0000EB0C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
