rule _TXT2COM_v2_06_uyybdy
{
	meta:
		description = "TXT2COM v2_06"
	strings:
		$a = {8D26????E8????B8????CD21CD2054585432434F4D20}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
