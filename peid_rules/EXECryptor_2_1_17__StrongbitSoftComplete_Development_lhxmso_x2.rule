rule _EXECryptor_2_1_17__StrongbitSoftComplete_Development_lhxmso
{
	meta:
		description = "EXECryptor 2_1_17 __ StrongbitSoftComplete Development"
	strings:
		$a = {BE????????B80000????8945FC89C28B460C09C00F84??00000001D089C350FF1594??????09C00F850F00000053FF1598??????09C00F84??0000008945F86A008F45F48B0609C08B55FC0F85030000008B461001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
