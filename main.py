# jessup_checker.py
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum

# Types & Data Classes
class ViolationType(Enum):
    NONE = "none"
    WARNING = "warning"
    ERROR = "error"

@dataclass
class CoverPageItem:
    present: bool
    found: str

@dataclass
class WordCount:
    count: int
    limit: int

    def get_percentage(self) -> float:
        return (self.count / self.limit) * 100

    def get_status(self) -> ViolationType:
        percentage = self.get_percentage()
        if percentage > 100:
            return ViolationType.ERROR
        elif percentage > 90:
            return ViolationType.WARNING
        return ViolationType.NONE

@dataclass
class AbbreviationInfo:
    count: int
    sections: List[str]

@dataclass
class MediaItem:
    section: str
    index: int
    text: str

@dataclass
class PenaltyItem:
    rule: str
    description: str
    points: int
    r: int
    details: str

# Main Checker Class
class JessupPenaltyChecker:
    def __init__(self):
        # Initialize with sample data
        self.data = {
            "memorialType": "Applicant",
            "coverPage": {
                "Team Number": {"present": True, "found": "349A"},
                "Court Name": {"present": True, "found": "International Court of Justice"},
                "Year": {"present": True, "found": "2025"},
                "Case Name": {"present": True, "found": "The Case Concerning The Naegea Sea"},
                "Memorial Type": {"present": True, "found": "Memorial for the Applicant"}
            },
            "memorialParts": {
                "Cover Page": True,
                "Table of Contents": True,
                "Index of Authorities": True,
                "Statement of Jurisdiction": True,
                "Statement of Facts": True,
                "Summary of Pleadings": True,
                "Pleadings": True,
                "Prayer for Relief": False
            },
            "wordCounts": {
                "Statement of Facts": {"count": 1196, "limit": 1200},
                "Summary of Pleadings": {"count": 642, "limit": 700},
                "Pleadings": {"count": 9424, "limit": 9500},
                "Prayer for Relief": {"count": 0, "limit": 200}
            },
            "abbreviations": {
                "ISECR": {"count": 2, "sections": ["Pleadings"]},
                "ICCPED": {"count": 1, "sections": ["Summary of Pleadings"]},
                "ICC": {"count": 1, "sections": ["Pleadings"]},
                "LOSC": {"count": 1, "sections": ["Pleadings"]},
                "AFRC": {"count": 1, "sections": ["Pleadings"]}
            },
            "media": [{"section": "Cover Page", "index": 6, "text": "----media/image1.png----"}]
        }
        
        self.penalties = [
            {
                "rule": "Rule 5.5",
                "description": "Missing Prayer for Relief",
                "points": 4,
                "r": 2,
                "details": "2 points per part"
            },
            {
                "rule": "Rule 5.17",
                "description": "Non-Permitted Abbreviations (5 found)",
                "points": 3,
                "r": 0,
                "details": "1 point each, max 3"
            },
            {
                "rule": "Rule 5.13",
                "description": "Improper Citation",
                "points": 3,
                "r": 0,
                "details": "1 point per violation, max 5"
            }
        ]

    def update_data(self, new_data: dict):
        """Update checker with new data"""
        self.data.update(new_data)

    def check_cover_page(self) -> Dict[str, CoverPageItem]:
        """Check cover page requirements"""
        return {
            key: CoverPageItem(value["present"], value["found"])
            for key, value in self.data["coverPage"].items()
        }

    def check_memorial_parts(self) -> Dict[str, bool]:
        """Check required memorial parts"""
        return self.data["memorialParts"]

    def check_word_counts(self) -> Dict[str, WordCount]:
        """Check word count limits"""
        return {
            section: WordCount(info["count"], info["limit"])
            for section, info in self.data["wordCounts"].items()
        }

    def check_abbreviations(self) -> Dict[str, AbbreviationInfo]:
        """Check for non-permitted abbreviations"""
        return {
            abbr: AbbreviationInfo(info["count"], info["sections"])
            for abbr, info in self.data["abbreviations"].items()
        }

    def check_media(self) -> List[MediaItem]:
        """Check for unapproved media"""
        return [MediaItem(**item) for item in self.data["media"]]

    def check_anonymity(self) -> bool:
        """Check for anonymity violations"""
        return True  # Example implementation

    def check_tracked_changes(self) -> bool:
        """Check for tracked changes"""
        return True  # Example implementation

    def check_citations(self) -> tuple[bool, int]:
        """Check for citation violations"""
        return False, 5  # Example: 5 violations found

    def check_plagiarism(self) -> bool:
        """Check for plagiarism"""
        return True  # Example implementation

    def calculate_total_penalties(self) -> int:
        """Calculate total penalty points"""
        return sum(penalty["points"] for penalty in self.penalties)

    def generate_report(self) -> dict:
        """Generate comprehensive check report"""
        word_counts = self.check_word_counts()
        cover_page = self.check_cover_page()
        memorial_parts = self.check_memorial_parts()
        abbreviations = self.check_abbreviations()
        media = self.check_media()
        
        return {
            "total_penalties": self.calculate_total_penalties(),
            "cover_page": {
                "status": all(item.present for item in cover_page.values()),
                "items": cover_page
            },
            "memorial_parts": {
                "status": all(memorial_parts.values()),
                "items": memorial_parts
            },
            "word_counts": {
                "status": all(wc.get_status() == ViolationType.NONE for wc in word_counts.values()),
                "items": word_counts
            },
            "abbreviations": {
                "status": len(abbreviations) == 0,
                "items": abbreviations
            },
            "media": {
                "status": len(media) == 0,
                "items": media
            },
            "anonymity": self.check_anonymity(),
            "tracked_changes": self.check_tracked_changes(),
            "citations": self.check_citations(),
            "plagiarism": self.check_plagiarism()
        }

    def print_report(self):
        """Print formatted penalty report"""
        report = self.generate_report()
        
        print("\n=== Jessup Memorial Penalty Checker ===\n")
        print(f"Total Penalty Points: {report['total_penalties']}\n")
        
        # Cover Page
        print("=== Cover Page Check ===")
        for key, item in report['cover_page']['items'].items():
            status = "✓" if item.present else "✗"
            print(f"{status} {key}: {item.found}")
        print()
        
        # Memorial Parts
        print("=== Memorial Parts ===")
        for part, present in report['memorial_parts']['items'].items():
            status = "✓" if present else "✗"
            print(f"{status} {part}")
        print()
        
        # Word Counts
        print("=== Word Count Analysis ===")
        for section, wc in report['word_counts']['items'].items():
            percentage = wc.get_percentage()
            status = wc.get_status()
            status_symbol = "!" if status == ViolationType.ERROR else "?" if status == ViolationType.WARNING else "✓"
            print(f"{status_symbol} {section}: {wc.count}/{wc.limit} words ({percentage:.1f}%)")
        print()
        
        # Abbreviations
        print("=== Abbreviations ===")
        for abbr, info in report['abbreviations']['items'].items():
            print(f"✗ {abbr} ({info.count} occurrences)")
            print(f"   Found in: {', '.join(info.sections)}")
        print()
        
        # Media
        print("=== Media Check ===")
        if report['media']['items']:
            for item in report['media']['items']:
                print(f"! Found in {item.section}: {item.text}")
        else:
            print("✓ No unapproved media found")
        print()
        
        # Other Checks
        print("=== Other Checks ===")
        print(f"{'✓' if report['anonymity'] else '✗'} Anonymity")
        print(f"{'✓' if report['tracked_changes'] else '✗'} Tracked Changes")
        citations_status, citations_count = report['citations']
        print(f"{'✓' if citations_status else '✗'} Citations ({citations_count} violations)")
        print(f"{'✓' if report['plagiarism'] else '✗'} Plagiarism")
        print()

def main():
    # Example usage
    checker = JessupPenaltyChecker()
    checker.print_report()

if __name__ == "__main__":
    main()
