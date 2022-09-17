rule _PECompact_2_0betastudent_version__Jeremy_Collake_txykch
{
	meta:
		description = "PECompact 2_0betastudent version __Jeremy Collake"
	strings:
		$a = {B8??????EE05121313125064FF350000000064892500}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
